import panel as pn
import param
from libs.rag import RAGService

class SourcesTab(param.Parameterized):
    """Document sources management tab"""
    
    def __init__(self, rag_service: RAGService):
        super().__init__()
        self.rag_service = rag_service
        
        # Input widgets
        self.source_input = pn.widgets.TextInput(
            placeholder="Enter PDF path, YouTube URL, or webpage URL..."
        )
        self.source_type = pn.widgets.Select(
            options=['pdf', 'youtube', 'web'],
            name='Source Type'
        )
        self.add_button = pn.widgets.Button(
            name="Add Source",
            button_type="primary"
        )
        self.status = pn.pane.Markdown("")
        
        self.add_button.on_click(self._handle_add)
        
    def create(self) -> pn.Column:
        """Create sources interface"""
        return pn.Column(
            pn.Row(pn.pane.Markdown("## Document Sources")),
            pn.Row(
                self.source_input,
                self.source_type,
                self.add_button
            ),
            self.status
        )
        
    def _handle_add(self, event):
        """Handle add source button click"""
        source = self.source_input.value
        source_type = self.source_type.value
        
        if not source:
            self.status.object = "⚠️ Please enter a source"
            return
            
        try:
            if self.rag_service.add_document(source, source_type):
                self.status.object = f"✅ Successfully added {source_type} source"
                self.source_input.value = ""
            else:
                self.status.object = "❌ Failed to add source"
        except Exception as e:
            self.status.object = f"❌ Error: {str(e)}" 