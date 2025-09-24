#include "pixmapmime.h"

PixmapMime::PixmapMime(QPixmap pix, QPoint offset, QString description)
    : QMimeData{},
    mPix{pix},
    mOffset{offset},
    mDescription{description}
{
    mMimeFormats << "text/html" << "text/plain";
}


QStringList PixmapMime::formats() const
{
    return mMimeFormats;
}

QVariant PixmapMime::retrieveData(const QString &mimetype, QMetaType preferredType) const
{
    if (mimetype == "text/plain") {
        return mDescription;
    }

    if (mimetype == "text/html") {
        QString htmlString;
        htmlString.append("<html><p>");
        htmlString.append(mDescription);
        htmlString.append("</p></html>");
        return htmlString;
    }

    return QMimeData::retrieveData(mimetype, preferredType);

}

QPoint PixmapMime::offset() const
{
    return mOffset;
}

QPixmap PixmapMime::pix() const
{
    return mPix;
}
