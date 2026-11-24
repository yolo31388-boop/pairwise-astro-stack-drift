import pytest
import imaging.astro_stack_drift as mod

CASES = [
    ("regional_distortion", (1,)),
    ("first_frame_reference", (1,)),
    ("dark_by_temp", (1,)),
    ("order_by_index", (1,)),
    ("sharpness_weight", (1,)),
    ("reject_trailed", (1,)),
    ("load_frames", (1,)),
    ("align", (1,)),
    ("stack", (1,)),
    ("export", (1,)),
    ("validate_snr", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
