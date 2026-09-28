"""Check the Python <-> Unity simulator link.

Sim version of course_files/scara/API/python_examples/scara_robot_test_script.py.
Start the simulator first (press Play, then Start Server), then run from the repo root:

    python tests/sim_connection_test.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hardware_api.sim_scara_motion_controller_api import sim_scara_motion_controller


def main():
    scara = sim_scara_motion_controller()  # 127.0.0.1:9000

    scara.SCARA_INITIALISE(0.125, 0.1, 0.095, 0.15, 1, 1.3, 0.01, 0.001, 1.3, 0.01, 0.001)

    scara.SCARA_MOVE_JOINT(2, 0, 1)
    scara.SCARA_MOVE_JOINT(3, -60, 1)
    scara.SCARA_MOVE_JOINT(0, 0, 1)
    scara.SCARA_MOVE_JOINT(1, 90, 1)

    print("[TEST] all commands acknowledged - Python <-> Unity link OK")


if __name__ == "__main__":
    main()
