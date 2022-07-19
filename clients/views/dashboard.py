from petstore.forms import AnimalForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from petstore.models import Animal


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class Dashboard(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_animal(self, id=None):
        animal = None

        if id is not None:
            animal = Animal.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not animal:
                raise Http404()

        return animal

    def render_animal(self, form):
        return render(
            self.request,
            'clients/pages/dashboard.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        animal = self.get_animal(id)
        form = AnimalForm(instance=animal)
        return self.render_recipe(form)

    def post(self, request, id=None):
        animal = self.get_animal(id)
        form = AnimalForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=animal
        )

        if form.is_valid():
            # Agora, o form é válido e eu posso tentar salvar
            animal = form.save(commit=False)

            animal.author = request.user
            animal.preparation_steps_is_html = False
            animal.is_published = False

            animal.save()

            messages.success(request, 'Sua receita foi salva com sucesso!')
            return redirect(
                reverse(
                    'dashboard_recipe_edit', args=(
                        animal.id,
                    )
                )
            )

        return self.render_animal(form)


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardDelete(Dashboard):
    def post(self, *args, **kwargs):
        animal = self.get_animal(self.request.POST.get('id'))
        animal.delete()
        messages.success(self.request, 'Deleted successfully.')
        return redirect(reverse('dashboard'))