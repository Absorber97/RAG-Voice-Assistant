import panel as pn
import param
from libs.voice import VoiceService

class VoiceTab(param.Parameterized):
    """Voice interface tab"""
    
    def __init__(self, voice_service: VoiceService):
        super().__init__()
        self.voice_service = voice_service
        self.status = pn.pane.Markdown("")
        self.transcript = pn.widgets.TextInput(disabled=True)
        
    def create(self) -> pn.Column:
        """Create voice tab interface"""
        
        # Voice controls
        controls = pn.Column(
            pn.Row(
                pn.pane.Markdown(f"### Wake Word: '{self.voice_service.wake_word}'"),
                pn.pane.Markdown("🎤 Listening...")
            ),
            pn.layout.Divider(),
            pn.Row(
                pn.pane.Markdown("Last Transcript:"),
                self.transcript
            ),
            pn.Row(self.status)
        )
        
        return pn.Column(
            pn.Row(pn.pane.Markdown("## Voice Interface")),
            controls
        ) 