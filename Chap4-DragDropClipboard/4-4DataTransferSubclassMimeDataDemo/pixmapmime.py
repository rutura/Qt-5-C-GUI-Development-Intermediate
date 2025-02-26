from PySide6.QtCore import QMimeData

class PixmapMime(QMimeData):
    """Custom QMimeData subclass that can store a pixmap and offset information"""
    
    def __init__(self, pix, offset, description):
        """
        Constructor for PixmapMime
        
        Args:
            pix (QPixmap): The pixmap to store
            offset (QPoint): The offset point (hotspot)
            description (str): A text description of the item
        """
        super().__init__()
        self.mPix = pix
        self.mOffset = offset
        self.description = description
        self.mimeFormats = ["text/html", "text/plain"]
    
    def pix(self):
        """Get the stored pixmap"""
        return self.mPix
    
    def offset(self):
        """Get the stored offset point"""
        return self.mOffset
    
    def formats(self):
        """Override to provide the supported MIME formats"""
        # In PySide6, we return a list of strings instead of QStringList
        return self.mimeFormats
    
    def retrieveData(self, mimetype, preferredType):
        """
        Override to provide data for each supported MIME type
        
        Args:
            mimetype (str): The requested MIME type
            preferredType (QMetaType): The preferred data type
        
        Returns:
            QVariant: The data in the requested format
        """
        if mimetype == "text/plain":
            return self.description
        elif mimetype == "text/html":
            html_string = "<html><p>" + self.description + "</p></html>"
            return html_string
        else:
            return super().retrieveData(mimetype, preferredType)