from anytree import NodeMixin, RenderTree, PreOrderIter


class Breadcrumb(NodeMixin):
    link = ""
    name = ""
    parents = []

    def __init__(self, p_name, p_link, parent=None, children=None):
        super(Breadcrumb, self).__init__()
        self.link = p_link
        self.name = p_name
        self.parent = parent
        if children:
            self.children = children


# Задаем иерархию навигации
def create_bread_crumb():
    main = Breadcrumb("Главная", "main:main")

    logstaf = Breadcrumb("Логи сотрудников", "mainapp:logstaf", parent=main)
    logproc = Breadcrumb("Логи процессов", "mainapp:logproc", parent=main)
    errdirupload = Breadcrumb("Ошибки интеграции", "mainapp:errdirupload", parent=main)
    editdevice = Breadcrumb("Устройства VM Client", "mainapp:editdevice", parent=main)
    editbtdevice = Breadcrumb("БТ устройства", "mainapp:editbtdevice", parent=main)
    deviceuser = Breadcrumb("Персонал", "mainapp:deviceuser", parent=main)
    editstaffroles = Breadcrumb("Роли персонала", "mainapp:editstaffroles", parent=main)
    faclility = Breadcrumb("Терминалы", "mainapp:editfacility", parent=main)
    editloc = Breadcrumb("Ячейки", "mainapp:editloc", parent=main)
    zones = Breadcrumb("Зоны", "mainapp:zones", parent=main)
    editdevtypes = Breadcrumb("Типы оборудования", "mainapp:editdevtypes", parent=main)
    editdevstatus = Breadcrumb("Статусы оборудования", "mainapp:editdevstatus", parent=main)
    editusersadm = Breadcrumb("Пользователи", "mainapp:editusersadm", parent=main)
    editusersgroup = Breadcrumb("Группы пользователей", "mainapp:editusersgroup", parent=main)
    editusersrol = Breadcrumb("Роли пользователей", "mainapp:editusersrol", parent=main)
    editcontenttype = Breadcrumb("Тип содержимого", "mainapp:editcontenttype", parent=main)
    editdevlist = Breadcrumb("Журнал устройств", "mainapp:editdevlist", parent=main)

    return main


# Конец иерархии навигации


def get_bread_crumb(p_link):
    main = create_bread_crumb()
    n = main

    for node in PreOrderIter(main):
        if node.link == p_link:
            n = node
            break

    result = []
    for i in node.iter_path_reverse():
        result.append(i)

    result.reverse()
    return result
