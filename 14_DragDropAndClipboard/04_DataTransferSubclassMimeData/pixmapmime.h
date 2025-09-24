#ifndef PIXMAPMIME_H
#define PIXMAPMIME_H

#include <QObject>
#include <QMimeData>
#include <QPixmap>

class PixmapMime : public QMimeData
{
    Q_OBJECT
public:
    explicit PixmapMime(QPixmap pix, QPoint offset, QString description);

signals:
    // QMimeData interface
public:
    QStringList formats() const override;

    QPixmap pix() const;

    QPoint offset() const;

protected:
    QVariant retrieveData(const QString &mimetype, QMetaType preferredType) const override;

private:
    QPixmap mPix;
    QPoint mOffset;
    QString mDescription;
    QStringList mMimeFormats;
};

#endif // PIXMAPMIME_H
