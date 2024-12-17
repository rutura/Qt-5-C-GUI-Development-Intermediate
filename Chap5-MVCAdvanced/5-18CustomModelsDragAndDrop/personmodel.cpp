#include "personmodel.h"
#include <QMimeData>

PersonModel::PersonModel(QObject *parent) : QAbstractListModel(parent)
{
    persons << "Donald Bush" << "Xi Jing Tao" <<
               "Vladmir Golbathev" <<
               "Emmanuel Mitterand" << "Jacob Mandela";
}

int PersonModel::rowCount(const QModelIndex &parent) const
{
    Q_UNUSED(parent);
    return  persons.size();
}


QVariant PersonModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();

    if (index.row() < 0 || index.row() >= persons.size())
        return QVariant();
    if (role == Qt::DisplayRole || role == Qt::EditRole)
        return persons.at(index.row());

    return  QVariant();
}

bool PersonModel::setData(const QModelIndex &index, const QVariant &value, int role)
{
    Q_UNUSED(role);

    if(index.isValid()){
        persons.replace(index.row(),value.toString());
        emit dataChanged(index,index);
        return true;
    }
    return  false;
}

QVariant PersonModel::headerData(int section, Qt::Orientation orientation, int role) const
{

    if (role != Qt::DisplayRole)
        return QVariant();

    if(orientation == Qt::Horizontal){
        if(section == 0){
            return "Names";
        }else{
            return  QVariant();
        }
    }

    return QVariant();

}

bool PersonModel::insertRows(int row, int count, const QModelIndex &parent)
{
    Q_UNUSED(parent);
    beginInsertRows(QModelIndex(), row, row+count-1);

    for (int i = 0; i < count; ++i) {
        persons.insert(row, "");
    }
    endInsertRows();
    return true;
}

bool PersonModel::removeRows(int row, int count, const QModelIndex &parent)
{
    Q_UNUSED(parent);
    beginRemoveRows(QModelIndex(), row, row+count-1);

    for (int i = 0; i < count; ++i) {
        persons.removeAt(row);
    }
    endRemoveRows();
    return true;
}

QStringList PersonModel::mimeTypes() const
{
    return QAbstractListModel::mimeTypes() << "plain/text";
}

QMimeData *PersonModel::mimeData(const QModelIndexList &indexes) const
{

    QStringList list;
    for( const QModelIndex & index : indexes){
        list << index.data().toString();
    }
    QMimeData * mimeData = QAbstractListModel::mimeData(indexes);
    mimeData->setText(list.join(","));

    return mimeData;
}

bool PersonModel::dropMimeData(const QMimeData *data, Qt::DropAction action,
                               int row, int column, const QModelIndex &parent)
{

    if(data->hasText()){

        if(parent.isValid()){
            //Ovewrite
            setData(parent,data->text(),Qt::DisplayRole);
        }else{
            //Add new data
            insertRows(rowCount(),1,QModelIndex());
            setData(index(rowCount()-1,0,QModelIndex()),data->text());

        }

        return true;
    }
    return QAbstractListModel::dropMimeData(data,action,row,column,parent);
}

Qt::ItemFlags PersonModel::flags(const QModelIndex &index) const
{
    if(!index.isValid()){
        return Qt::ItemIsEnabled | Qt::ItemIsDropEnabled;
    }else{
        return QAbstractListModel::flags(index) | Qt::ItemIsEditable | Qt::ItemIsDragEnabled |
                Qt::ItemIsDropEnabled;
    }
}
