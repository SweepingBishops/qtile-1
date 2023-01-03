from typing import Any, Optional

SURFACE_TARGET_KEY: Any

def from_buffer(obj: Any): ...

class Surface:
    _pointer: Any
    def __init__(self, pointer: Any, target_keep_alive: Optional[Any] = ...) -> None: ...
    def create_similar(self, content: Any, width: Any, height: Any): ...
    def create_similar_image(self, content: Any, width: Any, height: Any): ...
    def create_for_rectangle(self, x: Any, y: Any, width: Any, height: Any): ...
    def get_content(self): ...
    def has_show_text_glyphs(self): ...
    def set_device_offset(self, x_offset: Any, y_offset: Any) -> None: ...
    def get_device_offset(self): ...
    def set_fallback_resolution(self, x_pixels_per_inch: Any, y_pixels_per_inch: Any) -> None: ...
    def get_fallback_resolution(self): ...
    def get_font_options(self): ...
    def set_device_scale(self, x_scale: Any, y_scale: Any) -> None: ...
    def get_device_scale(self): ...
    def set_mime_data(self, mime_type: Any, data: Any) -> None: ...
    def get_mime_data(self, mime_type: Any): ...
    def supports_mime_type(self, mime_type: Any): ...
    def mark_dirty(self) -> None: ...
    def mark_dirty_rectangle(self, x: Any, y: Any, width: Any, height: Any) -> None: ...
    def show_page(self) -> None: ...
    def copy_page(self) -> None: ...
    def flush(self) -> None: ...
    def finish(self) -> None: ...
    def write_to_png(self, target: Optional[Any] = ...): ...

class ImageSurface(Surface):
    def __init__(
        self,
        format: Any,
        width: Any,
        height: Any,
        data: Optional[Any] = ...,
        stride: Optional[Any] = ...,
    ) -> None: ...
    @classmethod
    def create_for_data(
        cls, data: Any, format: Any, width: Any, height: Any, stride: Optional[Any] = ...
    ): ...
    @staticmethod
    def format_stride_for_width(format: Any, width: Any): ...
    @classmethod
    def create_from_png(cls, source: Any): ...
    def get_data(self): ...
    def get_format(self): ...
    def get_width(self): ...
    def get_height(self): ...
    def get_stride(self): ...

class RecordingSurface(Surface):
    def __init__(self, content: Any, extents: Any) -> None: ...
    def get_extents(self): ...
    def ink_extents(self): ...
