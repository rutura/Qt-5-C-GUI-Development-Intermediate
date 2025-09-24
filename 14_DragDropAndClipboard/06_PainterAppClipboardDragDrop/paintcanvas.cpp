#include "paintcanvas.h"
#include <QPainter>
#include <QMouseEvent>
#include <QMimeData>
#include <QFileInfo>
#include <QClipboard>
#include <QApplication>

PaintCanvas::PaintCanvas(QWidget *parent)
    : QWidget{parent}
{
    setAcceptDrops(true);
}

PaintCanvas::ToolType PaintCanvas::getTool() const
{
    return tool;
}

void PaintCanvas::setTool(ToolType newTool)
{
    tool = newTool;
}

bool PaintCanvas::getFill() const
{
    return fill;
}

void PaintCanvas::setFill(bool newFill)
{
    fill = newFill;
}

int PaintCanvas::getPenWidth() const
{
    return penWidth;
}

void PaintCanvas::setPenWidth(int newPenWidth)
{
    penWidth = newPenWidth;
}

QColor PaintCanvas::getPenColor() const
{
    return penColor;
}

void PaintCanvas::setPenColor(const QColor &newPenColor)
{
    penColor = newPenColor;
}

QColor PaintCanvas::getFillColor() const
{
    return fillColor;
}

void PaintCanvas::setFillColor(const QColor &newFillColor)
{
    fillColor = newFillColor;
}

void PaintCanvas::drawLineTo(const QPoint &endPoint)
{
    QPainter painter(&image);
    painter.setPen(QPen(penColor, penWidth, Qt::SolidLine, Qt::RoundCap,
                        Qt::RoundJoin));
    painter.setRenderHint(QPainter::Antialiasing, true);
    painter.drawLine(lastPoint, endPoint);

    int adjustment = penWidth + 2;

    //Force the paintEvent to draw the new stroke from lastPoint to endPoint
    update(QRect(lastPoint,endPoint).normalized().adjusted(-adjustment, -adjustment, +adjustment, +adjustment));

    lastPoint = endPoint;
}

void PaintCanvas::drawRectTo(const QPoint &endPoint, bool ellipse)
{
    QPainter painter(&image);
    painter.setPen(QPen(penColor, penWidth, Qt::SolidLine, Qt::RoundCap,
                        Qt::RoundJoin));


    if (fill)
        painter.setBrush(fillColor);
    else
        painter.setBrush(Qt::NoBrush);

    if(!ellipse)
        painter.drawRect(QRect(lastPoint, endPoint));
    else {
        painter.drawEllipse(QRect(lastPoint,endPoint));
    }

    //Erase the intermediary rectangle
    if(drawing){
        painter.setPen(QPen(Qt::white, penWidth+2, Qt::SolidLine, Qt::RoundCap,
                            Qt::RoundJoin));
        if(fill)
            painter.setBrush(Qt::white);
        else
            painter.setBrush(Qt::NoBrush);

        if(!ellipse)
            painter.drawRect(lastRect);
        else {
            painter.drawEllipse(lastRect);
        }


        //Reset the pen and brush
        painter.setPen(QPen(penColor, penWidth, Qt::SolidLine, Qt::RoundCap,
                            Qt::RoundJoin));
        painter.setBrush(fillColor);

    }

    lastRect = QRectF(lastPoint,endPoint);

    //Trigger a call to paintEvent
    update();

}

void PaintCanvas::eraseUnder(const QPoint &topLeft)
{
    QPainter painter(&image);

    //Erase the last eraser rectangle
    painter.setBrush(Qt::white);
    painter.setPen(Qt::white);
    painter.drawRect(lastEraserRect);

    //Erase the content under current eraser rect. Brush and pen still white
    QRect currentRect(topLeft,QSize(100,100));
    painter.setBrush(Qt::white);
    painter.setPen(Qt::white);
    painter.drawRect(currentRect);


    //Draw the current eraser rectangle in black
    painter.setBrush(Qt::black);
    painter.setPen(Qt::black);
    painter.drawRect(currentRect);


    //Store the last eraser rectangle
    lastEraserRect = currentRect;


    //Erase the eraser black rectangle when mouse release is triggered (when not drawing anymore)
    if(!drawing){
        painter.setBrush(Qt::white);
        painter.setPen(Qt::white);
        painter.drawRect(lastEraserRect);
        lastEraserRect = QRect(0,0,0,0);
    }

    //Call update to trigger the paint event
    update();

}

void PaintCanvas::resizeImage(QImage *image, const QSize &newSize)
{
    if (image->size() == newSize)
        return;

    QImage newImage(newSize, QImage::Format_RGB32);
    newImage.fill(qRgb(255, 255, 255));
    QPainter painter(&newImage);
    painter.drawImage(QPoint(0, 0), *image);
    *image = newImage;

}

bool PaintCanvas::isImage(const QString &fullpath) const
{
    const QFileInfo file(fullpath);
    const QString suffix = file.suffix().toLower();
    return suffix == "png" || suffix == "jpg" || suffix == "jpeg";
}

void PaintCanvas::copy()
{
    auto* mimeData = new QMimeData;
    mimeData->setImageData(image);
    QApplication::clipboard()->setMimeData(mimeData);
}

void PaintCanvas::paste()
{
    const QMimeData* mimeData = QApplication::clipboard()->mimeData();

    if (mimeData->hasUrls()) {
        const QList<QUrl>& urls = mimeData->urls();
        if (urls.count() != 1)
            return;

        const QFileInfo file(urls.at(0).toLocalFile());

        if (isImage(file.absoluteFilePath())) {
            QPixmap mPix(file.absoluteFilePath());
            QPainter painter(&image);
            painter.setPen(QPen(penColor, penWidth, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
            painter.setRenderHint(QPainter::Antialiasing, true);

            int drawWidth = width() - 10;
            int drawHeight = height() - 10;
            painter.drawPixmap(QRect(0, 0, drawWidth, drawHeight),
                               mPix.scaled(drawWidth, drawHeight),
                               QRect(0, 0, width(), height()));
            update();
        }
    }

}

void PaintCanvas::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton) {
        lastPoint = event->pos();
        drawing = true;
    }
    setFocus();
}

void PaintCanvas::mouseReleaseEvent(QMouseEvent *event)
{
        if (event->button() == Qt::LeftButton && drawing) {
            drawing = false;
            if (tool == ToolType::Pen) {
                drawLineTo(event->pos());
            }
            if (tool == ToolType::Rect) {
                drawRectTo(event->pos());
            }
            if (tool == ToolType::Ellipse) {
                drawRectTo(event->pos(),true);
            }
            if (tool == ToolType::Eraser) {
                eraseUnder(event->pos());
            }

            //Reset the last rect
            lastRect = QRect(0,0,0,0);
        }
}

void PaintCanvas::mouseMoveEvent(QMouseEvent *event)
{
        if ((event->buttons() & Qt::LeftButton) && drawing) {
            if (tool == ToolType::Pen) {
                drawLineTo(event->pos());
            }
            if (tool == ToolType::Rect) {
                drawRectTo(event->pos());
            }
            if (tool == ToolType::Ellipse) {
                drawRectTo(event->pos(),true);
            }
            if (tool == ToolType::Eraser) {
                eraseUnder(event->pos());
            }


        }
}

void PaintCanvas::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    QRect rectToDraw = event->rect();
    painter.drawImage(rectToDraw, image, rectToDraw);

}

void PaintCanvas::resizeEvent(QResizeEvent *event)
{
    if (width() > image.width() || height() > image.height()) {
        int newWidth = qMax(width() + 128, image.width());
        int newHeight = qMax(height() + 128, image.height());
        resizeImage(&image, QSize(newWidth, newHeight));
        update();
    }
    QWidget::resizeEvent(event);
}


void PaintCanvas::dragEnterEvent(QDragEnterEvent *event)
{
    if (event->mimeData()->hasUrls()) {
        const QList<QUrl>& urls = event->mimeData()->urls();

        // Check if at least one URL points to an image file
        for (const QUrl& url : urls) {
            const QFileInfo file(url.toLocalFile());
            if (isImage(file.absoluteFilePath())) {
                event->acceptProposedAction();
                return;
            }
        }
    }
}

void PaintCanvas::dropEvent(QDropEvent *event)
{
    if (event->mimeData()->hasUrls()) {
        const QList<QUrl>& urls = event->mimeData()->urls();

        // Process the first valid image file found
        for (const QUrl& url : urls) {
            const QFileInfo file(url.toLocalFile());
            if (isImage(file.absoluteFilePath())) {
                QPixmap droppedPixmap(file.absoluteFilePath());
                if (!droppedPixmap.isNull()) {
                    QPainter painter(&image);
                    painter.setRenderHint(QPainter::Antialiasing, true);

                    // Draw the image at the top-left corner (0, 0)
                    // Use the canvas widget size for the dropped image
                    int drawWidth = width() - 10;
                    int drawHeight = height() - 10;
                    painter.drawPixmap(QRect(0, 0, drawWidth, drawHeight),
                                       droppedPixmap.scaled(drawWidth, drawHeight),
                                       QRect(0, 0, width(), height()));
                    update();
                    event->acceptProposedAction();
                    qDebug() << "Image dropped and drawn at top-left corner";
                    return;
                }
            }
        }
    }
}

void PaintCanvas::keyPressEvent(QKeyEvent *event)
{
    if (event->matches(QKeySequence::Copy)) {
        qDebug() << "Copy sequence detected";
        copy();
        event->accept();
    } else if (event->matches(QKeySequence::Paste)) {
        qDebug() << "Paste sequence detected";
        paste();
        event->accept();
    } else {
        QWidget::keyPressEvent(event);
    }
}
