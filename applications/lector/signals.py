def update_libro_stock(sender, instance, **kwargs):
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()