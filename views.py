import io
from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ui import Select, View
from quizzes import QUIZZES
from config import FONT_PATH

class QuizDropdown(Select):
    def __init__(self, quiz, user, language, bot):
        self.quiz = quiz
        self.user = user
        self.language = language
        self.bot = bot
        self.score = 0
        self.current_question = 0
        self.user_answers = []

        options = [
            discord.SelectOption(label=option, value=f"option_{i}") for i, option in enumerate(self.quiz[self.current_question]["options"])
        ]

        super().__init__(placeholder=self.quiz[self.current_question]["title"],
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_answer = self.values[0]
        correct_answer = self.quiz[self.current_question]["answer"]

        self.user_answers.append((self.quiz[self.current_question]["question"],
                                  selected_answer, correct_answer))

        if selected_answer == f"option_{self.quiz[self.current_question]['options'].index(correct_answer)}":
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.quiz):
            next_question = self.quiz[self.current_question]["question"]
            next_options = [
                discord.SelectOption(label=option, value=f"option_{i}")
                for i, option in enumerate(self.quiz[self.current_question]["options"])
            ]
            new_select = discord.ui.Select(placeholder=next_question,
                                           min_values=1,
                                           max_values=1,
                                           options=next_options)
            view = discord.ui.View()
            view.add_item(new_select)
            new_select.callback = self.callback

            await interaction.response.edit_message(
                content=f"**{next_question}**", view=view)
        else:
            await self.send_results()

    async def send_results(self):
        result_message = f"**Quiz Complete! Your score is: {self.score}/{len(self.quiz)}**\n\n"
        for i, (title, user_answer, correct_answer) in enumerate(self.user_answers):
            user_answer_label = self.quiz[i]['options'][int(user_answer.split('_')[-1])]
            if user_answer_label == correct_answer:
                result_message += f"**Q{i+1}:** _{title}_\nYour answer: `{user_answer_label}` ✅\nCorrect answer: `{correct_answer}` ✅\n\n"
            else:
                result_message += f"**Q{i+1}:** _{title}_\nYour answer: `{user_answer_label}` ❌\nCorrect answer: `{correct_answer}` ✅\n\n"

        for chunk in [result_message[i:i + 2000] for i in range(0, len(result_message), 2000)]:
            await self.user.send(chunk)

        await self.user.send(f"\n # ***Please enter your legal name for the certificate! If you have misspelled it, please DM an Administrator.***")

        def check(msg):
            return msg.author.id == self.user.id and isinstance(msg.channel, discord.DMChannel)

        response_msg = await self.bot.wait_for('message', check=check)
        print(f"User {self.user.name} provided the legal name: {response_msg.content}")

        user_name = response_msg.content

        # Define the image path based on the chosen language
        image_path = f"{self.language.lower()}.png"

        # Open the local image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT_PATH, 60)

        # Get image dimensions
        width, height = image.size
        text = user_name

        # Calculate text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate text position (center of the image)
        x = (width - text_width) / 2
        y = ((height - text_height) / 2) + 67.5
        draw.text((x, y), text, font=font, fill="black")

        x = ((width - text_width) / 2) + 450
        y = ((height - text_height) / 2) + 290
        font = ImageFont.truetype(FONT_PATH, 50)
        draw.text((x, y), str(self.score), font=font, fill="black")

        # Save the modified image to a BytesIO object
        output_image = io.BytesIO()
        image.save(output_image, format='PNG')
        output_image.seek(0)  # Go to the start of the BytesIO object

        # Send the image to the user
        await self.user.send(file=discord.File(output_image, 'cert_with_name.png'))

        # Send note to the user
        await self.user.send("**\n Note: This Certificate Is A Basic Level Certificate! If You Want To Upgrade It Plsease Create A Ticket At .gg/devscert And Show The Certificate You Got!**")


class DropdownView(View):
    def __init__(self, quiz, user, language, bot):
        super().__init__()
        self.add_item(QuizDropdown(quiz, user, language, bot))


class LanguageDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Python", description="Get certified in Python!"),
            discord.SelectOption(label="Lua", description="Get certified in Lua!"),
            # Add more languages here...
        ]

        super().__init__(placeholder='Choose a programming language...',
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):
        language = self.values[0]
        await interaction.response.send_message(f'Check your DMs for the {language} quiz!')

        quiz = QUIZZES.get(language)
        if quiz:
            await interaction.user.send(
                f"Starting your {language} quiz!\n**{quiz[0]['question']}**",
                view=DropdownView(quiz, interaction.user, language, interaction.client))


class LanguageDropdownView(View):
    def __init__(self):
        super().__init__()
        self.add_item(LanguageDropdown())
