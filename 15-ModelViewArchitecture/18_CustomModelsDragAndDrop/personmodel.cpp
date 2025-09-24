#include "personmodel.h"
#include <QMimeData>

PersonModel::PersonModel(QObject *parent)
    : QAbstractListModel{parent}
{
    persons << "Donald bush" << "Xi Jing Tao"
            << "Vladmir Golbathev"
            << "Emmanuel Mitterand" << "Jacob Mandela";
}


int PersonModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return persons.size();
}

QVariant PersonModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();

    if (index.row() < 0 || index.row() >= persons.size())
        return QVariant();

    if( role == Qt::DisplayRole || role == Qt::EditRole)
        return persons.at(index.row());

    return QVariant();
}

bool PersonModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    if (!index.isValid())
        return false;
    //Set the data to the model
    persons.replace(index.row(),value.toString());
    emit dataChanged(index,index);
    return true;
}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (role != Qt::DisplayRole)
        return QVariant();

    if (orientation == Qt::Horizontal && section == 0) {
        return "Names";
    }

    return QVariant();
}

bool PersonModel::insertRows(int row, int count, const QModelIndex &parent)
{
    Q_UNUSED(parent);
    beginInsertRows(QModelIndex(), row, row + count - 1);

    for (int i = 0; i < count; ++i) {
        persons.insert(row, "");
    }
    endInsertRows();
    return true;
}

bool PersonModel::removeRows(int row, int count, const QModelIndex &parent)
{
    Q_UNUSED(parent);
    beginRemoveRows(QModelIndex(), row, row + count - 1);

    for (int i = 0; i < count; ++i) {
        persons.removeAt(row);
    }
    endRemoveRows();
    return true;
}

QStringList PersonModel::mimeTypes() const
{

    //We support plain text for drag and drop
    return QAbstractListModel::mimeTypes() << "text/plain";
}

//Package the data when a drag is initiated
QMimeData *PersonModel::mimeData(const QModelIndexList &indexes) const
{
    QStringList list;
    for(const QModelIndex & index: indexes){
        list << index.data().toString();
    }
    QMimeData * mimeData = QAbstractListModel::mimeData(indexes);
    mimeData->setText(list.join(","));
    return mimeData;
}

//Handle data that is droped.
bool PersonModel::dropMimeData(const QMimeData *data, Qt::DropAction action, int row, int column, const QModelIndex &index)
{

    if(data->hasText()){

        if(index.isValid()){
            //Overwrite
            setData(index,data->text(), Qt::DisplayRole);
        }else{
            //Add a new piece of data
            insertRows(rowCount(QModelIndex()), 1, QModelIndex());
            QModelIndex newIndex = this->index(rowCount(QModelIndex()) - 1, 0);
            setData(newIndex,data->text(),Qt::DisplayRole);
        }
        return true;
    }
    return QAbstractListModel::dropMimeData(data,action,row,column,index);

}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const
{
    if (!index.isValid()) {
        return Qt::ItemIsEnabled | Qt::ItemIsDropEnabled;
    }
    return QAbstractListModel::flags(index) | Qt::ItemIsEditable
                                        | Qt::ItemIsDragEnabled | Qt::ItemIsDropEnabled;
}
