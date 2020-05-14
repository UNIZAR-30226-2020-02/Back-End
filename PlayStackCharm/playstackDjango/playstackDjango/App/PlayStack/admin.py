from django.contrib import admin

from playstackDjango.App.PlayStack.models import *

from django.contrib.admin import SimpleListFilter
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Premium)
#admin.site.register(NoPremium)
admin.site.register(CreadorContenido)
admin.site.register(Audio)
admin.site.register(Cancion)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(PlayList)
admin.site.register(Carpeta)
admin.site.register(Podcast)
admin.site.register(Capitulo)
admin.site.register(Interlocutor)
admin.site.register(AudioEscuchado)
admin.site.register(Relacion)
admin.site.register(Peticiones)






from django.contrib import admin

class NoPremiumListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'pidePremium'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pidePremium'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_species = []
        list_of_species.append(('False', False))
        list_of_species.append(('True', True))
        return list_of_species
    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(pidePremium=self.value())
        return queryset



@admin.register(NoPremium)
class NoPremiumAdmin(admin.ModelAdmin):
    list_display = ('UsuarioRegistrado', 'pidePremium', )
    list_filter = (NoPremiumListFilter, )

    actions = ['toPremium']
    def toPremium(self, request, queryset):
        for i in queryset:
            user=i.UsuarioRegistrado
            Premium.objects.create(UsuarioRegistrado=user)
            i.delete()


