"""This is for the UI and somethings like it"""

import flet as ft

#Personal Use
from module.audio import audio

class Utils():
    """Everything than you need"""
    
    async def transcription(link: str):
        """TODO: MAKE THIS VERY GREAT"""
        await audio.download(link=link)


class UI():
    """User Interface"""
    async def main(page: ft.Page):
        await page.update_async()

        async def x(e):
            await Utils.transcription(link=urlText.value)

        urlText = ft.TextField(width=800)
        transcriptButton = ft.TextButton(text="Transcript", on_click=x)

        await page.add_async(
            ft.Row(
                [
                    urlText,
                    transcriptButton
                ]
            )
        )

    ft.app(target=main, view=ft.AppView.FLET_APP)

UI()