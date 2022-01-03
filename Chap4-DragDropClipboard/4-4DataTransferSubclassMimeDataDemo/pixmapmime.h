#ifndef PIXMAPMIME_H
#define PIXMAPMIME_H

#include <QMimeData>
#include <QPixmap>

class PixmapMime : public QMimeData
{
    Q_OBJECT
public:
    explicit PixmapMime(QPixmap pix,QPoint offset,QString description);

    QPixmap pix() const;

    QPoint offset() const;

signals:

public slots:
private:
    QPixmap mPix;
    QPoint mOffset;
    QString description;
    QStringList mimeFormats;

    // QMimeData interface
public:
    QStringList formats() const override;

protected:
    QVariant retrieveData(const QString &mimetype, QVariant::Type preferredType) const override;
};

#endif // PIXMAPMIME_H
