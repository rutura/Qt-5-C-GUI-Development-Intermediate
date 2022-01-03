#include "pixmapmime.h"

PixmapMime::PixmapMime(QPixmap pix,QPoint offset,QString description)  :
    mPix(pix),mOffset(offset),description(description)
{
    mimeFormats << "text/html" << "text/plain";
}

QPixmap PixmapMime::pix() const
{
    return mPix;
}

QPoint PixmapMime::offset() const
{
    return mOffset;
}

QStringList PixmapMime::formats() const
{
    return  mimeFormats;
}

QVariant PixmapMime::retrieveData(const QString &mimetype, QVariant::Type preferredType) const
{

    if(mimetype == "text/plain"){
        return  description;
    }else if(mimetype == "text/html"){
        QString htmlString ;
        htmlString.append( "<html><p>" );
        htmlString.append(description) ;
        htmlString.append("</p></html>");

        return  htmlString;

    }else {
        return  QMimeData::retrieveData(mimetype,preferredType);

    }
}
