import cv2
from runner import is_snap


def test_actual_snaps():
    test_files = ["tests/actual/%s.png" % i for i in range(1, 8)]
    for f in test_files:
        img = cv2.imread(f, 0)
        assert is_snap(img)


def non_snaps():
    test_files = ["tests/not/%s.jpg" % i for i in range(1, 7)]
    for f in test_files:
        img = cv2.imread(f, 0)
        assert not is_snap(img)
