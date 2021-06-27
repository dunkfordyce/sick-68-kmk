import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.keys import KC

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP2, board.GP3, board.GP4, board.GP6, board.GP7, board.GP8, board.GP10, board.GP11, board.GP12, board.GP14, board.GP15, board.GP16, board.GP18, board.GP19, board.GP20)
    row_pins = (board.GP1, board.GP5, board.GP9, board.GP13, board.GP17)
    diode_orientation = DiodeOrientation.COLUMNS
    
keyboard = KMKKeyboard()
#keyboard.debug_enabled = True
_______ = KC.TRNS
XXXXXXX = KC.NO
BASE = 0
FN1 = 1
LAYER1 = KC.MO(FN1)
keyboard.keymap = [
    [
        KC.GESC, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,  KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.GRAVE,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,   KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,   KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, XXXXXXX, KC.ENT,  KC.PGUP,
        KC.LSFT, XXXXXXX, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.PGDOWN,
        KC.LCTL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, XXXXXXX, KC.RALT, LAYER1,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [
        _______, KC.F1  , KC.F2  , KC.F3  , KC.F4  , KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10 , KC.F11 , KC.F12 , _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, KC.LEFT, KC.RIGHT, KC.DOWN, KC.UP, _______, _______, XXXXXXX, _______, _______,
        _______, XXXXXXX, _______, _______, _______, _______, _______, _______, _______, KC.VOLD, KC.VOLU, _______, _______, _______, _______,
        _______, _______, _______, XXXXXXX, XXXXXXX, XXXXXXX, _______, XXXXXXX, XXXXXXX, _______, _______, _______, _______, _______, _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()
