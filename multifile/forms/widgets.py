from django import forms

class MultiFileInput(forms.widgets.FileInput):
    """A multiple-file file input widget."""

    class Media:
        js = ('js/multifile.js', )

    def render(self, name, value, attrs=None):
        """Render as usual, but with added `multiple` attribute."""
        if attrs is None:
            attrs = {}

        attrs.setdefault('multiple', 'multiple')

        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        """Return a list of the uploaded files."""
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return []
