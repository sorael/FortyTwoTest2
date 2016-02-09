from django.core.management.base import NoArgsCommand
from django.db.models import get_models


class Command(NoArgsCommand):
    help = 'Prints all project models and the count of objects in every model'

    def handle_noargs(self, **options):
        for model in get_models():
            count = model.objects.count()
            self.stdout.write(self.write_output(count, model))
            self.stderr.write(self.write_output(count, model, error=True))

    def write_output(self, count, model, error=False):
        if error:
            pre = 'error: '
        else:
            pre = ''
        return '%sName: %s. Objects count: %s.' % (pre, model.__name__, count)
