import numpy as np


def projection_matrix(W, H, n, f, fx, fy, ox, oy):
    return np.array([
        [2 * fx / W, 0,          (W - 2 * ox) / W,   0],
        [0,          2 * fy / H, (-H + 2 * oy) / H,  0],
        [0,          0,          -(f + n) / (f - n), -2 * f * n / (f - n)],
        [0,          0,          -1,                 0],
    ])


def camera_point_to_pixel(P_C, W, H, n, f, fx, fy, ox, oy):
    M_proj = projection_matrix(W, H, n, f, fx, fy, ox, oy)

    P_clip = M_proj @ np.array(P_C, dtype=float)
    w_clip = P_clip[3]
    P_ndc = P_clip[:3] / w_clip

    x_ndc, y_ndc, z_ndc = P_ndc
    u = 0.5 * (x_ndc + 1.0) * W
    v = 0.5 * (y_ndc + 1.0) * H

    return {
        "M_proj": M_proj,
        "P_clip": P_clip,
        "P_ndc": P_ndc,
        "pixel": (u, v),
    }


if __name__ == "__main__":
    result = camera_point_to_pixel(
        P_C=(0.3, -0.15, -6.0, 1.0),
        W=800, H=600, n=0.2, f=20,
        fx=800, fy=800, ox=400, oy=400,
    )
    print("M_proj =\n", result["M_proj"])
    print("P_clip =", result["P_clip"])
    print("P_ndc  =", result["P_ndc"])
    print("pixel (u, v) =", result["pixel"])
