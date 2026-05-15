import importlib
import warnings

try:
    te = importlib.import_module('typing_extensions')
except Exception:
    te = None

if te is not None and not hasattr(te, 'TypeAliasType'):
    # Provide a lightweight compatibility fallback for environments
    # where packages expect `TypeAliasType` to exist.
    class _TypeAliasType:  # minimal placeholder
        pass

    setattr(te, 'TypeAliasType', _TypeAliasType)
    warnings.warn('Patched typing_extensions.TypeAliasType for compatibility', RuntimeWarning)
