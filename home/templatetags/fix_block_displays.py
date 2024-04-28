from __future__ import annotations

from django import template

register = template.Library()


@register.filter
def heading_size_to_tag(size):
    """Converts headings saved with tailwind text size to HTML heading tag."""
    if size in ["text-5xl", "text-4xl", "text-3xl", "text-2xl", "text-xl", "text-lg"]:
        tag_mapping = {
            "text-5xl": "h1",
            "text-4xl": "h2",
            "text-3xl": "h3",
            "text-2xl": "h4",
            "text-xl": "h5",
            "text-lg": "h6",
        }
        return tag_mapping.get(size, "h6")
    return size


@register.filter
def get_css_class(size):
    css_classes = {
        "h1": "text-5xl",
        "h2": "text-4xl",
        "h3": "text-3xl",
        "h4": "text-2xl",
        "h5": "text-xl",
        "h6": "text-lg",
    }
    return css_classes.get(size, "text-lg")
