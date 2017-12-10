def filterByAttribute(modelName, filterKeys):
    return modelName.objects.get(**filterKeys)

def filterAttribute(modelName, filterKeys):
    return modelName.objects.filter(**filterKeys)

def fetchAll(modelName):
    return modelName.objects.all()