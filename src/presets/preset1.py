from midisport.preset.preset import Preset

def get() -> Preset:
    preset1 = Preset()
    preset1.set_id(1)
    preset1.set_name('port 1')
    preset1.set_patch_number(1)
    preset1.set_value({
        '1': [2],
        '2': [2, 4],
        '3': [3, 4, 5],
        '4': [7],
        '5': [2, 3, 4],
        '6': [4, 5, 6],
        '7': [8],
        '8': [1, 8],
    })
    return preset1
