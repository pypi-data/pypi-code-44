import autoarray as aa
import numpy as np
import pytest
import scipy.spatial


class TestRectangularGrid:
    
    class TestGridNeighbors:
        def test__3x3_grid__buffer_is_small__grid_give_min_minus_1_max_1__sets_up_geometry_correctly(
            self
        ):

            grid = np.array(
                [
                    [1.0, -1.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [0.0, -1.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [-1.0, -1.0],
                    [-1.0, 0.0],
                    [-1.0, 1.0],
                ]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(3, 3), grid=grid, buffer=1e-8)

            assert pix_grid.shape_2d == (3, 3)
            assert pix_grid.pixel_scales == pytest.approx((2.0 / 3.0, 2.0 / 3.0), 1e-2)
            assert (pix_grid.pixel_neighbors[0] == [1, 3, -1, -1]).all()
            assert (pix_grid.pixel_neighbors[1] == [0, 2, 4, -1]).all()
            assert (pix_grid.pixel_neighbors[2] == [1, 5, -1, -1]).all()
            assert (pix_grid.pixel_neighbors[3] == [0, 4, 6, -1]).all()
            assert (pix_grid.pixel_neighbors[4] == [1, 3, 5, 7]).all()
            assert (pix_grid.pixel_neighbors[5] == [2, 4, 8, -1]).all()
            assert (pix_grid.pixel_neighbors[6] == [3, 7, -1, -1]).all()
            assert (pix_grid.pixel_neighbors[7] == [4, 6, 8, -1]).all()
            assert (pix_grid.pixel_neighbors[8] == [5, 7, -1, -1]).all()

            assert (
                pix_grid.pixel_neighbors_size == np.array([2, 3, 2, 3, 4, 3, 2, 3, 2])
            ).all()

        def test__3x3_grid__same_as_above_change_buffer(self):

            grid = np.array(
                [
                    [-1.0, -1.0],
                    [-1.0, 0.0],
                    [-1.0, 1.0],
                    [0.0, -1.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [1.0, -1.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                ]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(3, 3), grid=grid, buffer=1e-8)

            assert pix_grid.shape_2d == (3, 3)
            assert pix_grid.pixel_scales == pytest.approx((2.0 / 3.0, 2.0 / 3.0), 1e-2)

        def test__5x4_grid__buffer_is_small(self):

            grid = np.array(
                [
                    [1.0, -1.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [0.0, -1.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [-1.0, -1.0],
                    [-1.0, 0.0],
                    [-1.0, 1.0],
                ]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(5, 4), grid=grid, buffer=1e-8)

            assert pix_grid.shape_2d == (5, 4)
            assert pix_grid.pixel_scales == pytest.approx((2.0 / 5.0, 2.0 / 4.0), 1e-2)

        def test__3x3_grid__larger_range_of_grid(self):

            grid = np.array(
                [[2.0, 1.0], [4.0, 3.0], [6.0, 5.0], [8.0, 7.0]]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(3, 3), grid=grid, buffer=1e-8)

            assert pix_grid.shape_2d == (3, 3)
            assert pix_grid.pixel_scales == pytest.approx((6.0 / 3.0, 6.0 / 3.0), 1e-2)

    class TestPixelCentres:
        def test__3x3_grid__pixel_centres(self):

            grid = np.array(
                [
                    [1.0, -1.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [0.0, -1.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [-1.0, -1.0],
                    [-1.0, 0.0],
                    [-1.0, 1.0],
                ]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(3, 3), grid=grid, buffer=1e-8)

            assert pix_grid == pytest.approx(
                np.array(
                    [
                        [2.0 / 3.0, -2.0 / 3.0],
                        [2.0 / 3.0, 0.0],
                        [2.0 / 3.0, 2.0 / 3.0],
                        [0.0, -2.0 / 3.0],
                        [0.0, 0.0],
                        [0.0, 2.0 / 3.0],
                        [-2.0 / 3.0, -2.0 / 3.0],
                        [-2.0 / 3.0, 0.0],
                        [-2.0 / 3.0, 2.0 / 3.0],
                    ]
                )
            )

        def test__4x3_grid__pixel_centres(self):

            grid = np.array(
                [
                    [1.0, -1.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [0.0, -1.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [-1.0, -1.0],
                    [-1.0, 0.0],
                    [-1.0, 1.0],
                ]
            )

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(4, 3), grid=grid, buffer=1e-8)

            assert pix_grid == pytest.approx(
                np.array(
                    [
                        [0.75, -2.0 / 3.0],
                        [0.75, 0.0],
                        [0.75, 2.0 / 3.0],
                        [0.25, -2.0 / 3.0],
                        [0.25, 0.0],
                        [0.25, 2.0 / 3.0],
                        [-0.25, -2.0 / 3.0],
                        [-0.25, 0.0],
                        [-0.25, 2.0 / 3.0],
                        [-0.75, -2.0 / 3.0],
                        [-0.75, 0.0],
                        [-0.75, 2.0 / 3.0],
                    ]
                )
            )

    class TestPixelNeighbors:
        def test__compare_to_pixelization_util(self):
            # |0 | 1| 2| 3|
            # |4 | 5| 6| 7|
            # |8 | 9|10|11|
            # |12|13|14|15|

            pix_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(7, 5), grid=np.zeros((2,2)), buffer=1e-8)

            pixel_neighbors_util, pixel_neighbors_size_util = aa.util.pixelization.rectangular_neighbors_from_shape(
                shape=(7, 5)
            )

            assert (pix_grid.pixel_neighbors == pixel_neighbors_util).all()
            assert (pix_grid.pixel_neighbors_size == pixel_neighbors_size_util).all()

    class TestPixelSignals:
        def test__pixel_signals__compare_to_mapper_util(self, grid_7x7, image_7x7):

            pixelization_grid = aa.pix_grid.RectangularGrid.from_shape_2d_and_grid(shape_2d=(3,3), grid=grid_7x7)

            mapper = aa.mappers.RectangularMapper(
                grid=grid_7x7,
                pixelization_grid=pixelization_grid,
                hyper_image=image_7x7,
            )

            pixel_signals = mapper.pixel_signals_from_signal_scale(signal_scale=2.0)

            pixel_signals_util = aa.util.mapper.adaptive_pixel_signals_from_images(
                pixels=9,
                signal_scale=2.0,
                pixelization_1d_index_for_sub_mask_1d_index=mapper.pixelization_1d_index_for_sub_mask_1d_index,
                mask_1d_index_for_sub_mask_1d_index=grid_7x7.regions._mask_1d_index_for_sub_mask_1d_index,
                hyper_image=image_7x7,
            )

            assert (pixel_signals == pixel_signals_util).all()


class TestVoronoi:
    class TestVoronoiGrid:
        def test__9_points___check_voronoi_swaps_axis_from_y_x__to_x_y(self):
            # 9 points in a square - makes a square (this is the example int he scipy documentaiton page)

            grid = np.array(
                [
                    [2.0, 0.0],
                    [2.0, 1.0],
                    [2.0, 2.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [1.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 2.0],
                ]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)

            assert (
                pix.voronoi.points
                == np.array(
                    [
                        [0.0, 2.0],
                        [1.0, 2.0],
                        [2.0, 2.0],
                        [0.0, 1.0],
                        [1.0, 1.0],
                        [2.0, 1.0],
                        [0.0, 0.0],
                        [1.0, 0.0],
                        [2.0, 0.0],
                    ]
                )
            ).all()

        def test__points_in_x_cross_shape__sets_up_diamond_voronoi_vertices(self):
            # 5 points in the shape of the face of a 5 on a die - makes a diamond Voronoi diagram

            grid = np.array(
                [[-1.0, 1.0], [1.0, 1.0], [0.0, 0.0], [-1.0, -1.0], [1.0, -1.0]]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)

            pix.voronoi.vertices = list(map(lambda x: list(x), pix.voronoi.vertices))

            assert [0, 1.0] in pix.voronoi.vertices
            assert [-1.0, 0.0] in pix.voronoi.vertices
            assert [1.0, 0.0] in pix.voronoi.vertices
            assert [0.0, -1.0] in pix.voronoi.vertices

        def test__9_points_in_square___sets_up_square_of_voronoi_vertices(self):
            # 9 points in a square - makes a square (this is the example int he scipy documentaiton page)

            grid = np.array(
                [
                    [2.0, 0.0],
                    [2.0, 1.0],
                    [2.0, 2.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [1.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 2.0],
                ]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)

            # ridge points is a numpy array for speed, but convert to list for the comparisons below so we can use in
            # to look for each list

            pix.voronoi.vertices = list(map(lambda x: list(x), pix.voronoi.vertices))

            assert [0.5, 1.5] in pix.voronoi.vertices
            assert [1.5, 0.5] in pix.voronoi.vertices
            assert [0.5, 0.5] in pix.voronoi.vertices
            assert [1.5, 1.5] in pix.voronoi.vertices

        def test__points_in_x_cross_shape__sets_up_pairs_of_voronoi_cells(self):
            # 5 points in the shape of the face of a 5 on a die - makes a diamond Voronoi diagram

            grid = np.array(
                [[1.0, -1.0], [1.0, 1.0], [0.0, 0.0], [-1.0, -1.0], [-1.0, 1.0]]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)
            # ridge points is a numpy array for speed, but convert to list for the comparisons below so we can use in
            # to look for each list

            pix.voronoi.ridge_grid = list(map(lambda x: list(x), pix.voronoi.ridge_points))

            assert len(pix.voronoi.ridge_points) == 8

            assert [2, 0] in pix.voronoi.ridge_points or [0, 2] in pix.voronoi.ridge_points
            assert [2, 1] in pix.voronoi.ridge_points or [1, 2] in pix.voronoi.ridge_points
            assert [2, 3] in pix.voronoi.ridge_points or [3, 2] in pix.voronoi.ridge_points
            assert [2, 4] in pix.voronoi.ridge_points or [4, 2] in pix.voronoi.ridge_points
            assert [0, 1] in pix.voronoi.ridge_points or [1, 0] in pix.voronoi.ridge_points
            assert [0.3] in pix.voronoi.ridge_points or [3, 0] in pix.voronoi.ridge_points
            assert [3, 4] in pix.voronoi.ridge_points or [4, 3] in pix.voronoi.ridge_points
            assert [4, 1] in pix.voronoi.ridge_points or [1, 4] in pix.voronoi.ridge_points

        def test__9_points_in_square___sets_up_pairs_of_voronoi_cells(self):
            # 9 points in a square - makes a square (this is the example int he scipy documentaiton page)

            grid = np.array(
                [
                    [2.0, 0.0],
                    [2.0, 1.0],
                    [2.0, 2.0],
                    [1.0, 0.0],
                    [1.0, 1.0],
                    [1.0, 2.0],
                    [0.0, 0.0],
                    [0.0, 1.0],
                    [0.0, 2.0],
                ]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)

            # ridge points is a numpy array for speed, but convert to list for the comparisons below so we can use in
            # to look for each list

            pix.voronoi.ridge_grid = list(map(lambda x: list(x), pix.voronoi.ridge_points))

            assert len(pix.voronoi.ridge_points) == 12

            assert [0, 1] in pix.voronoi.ridge_points or [1, 0] in pix.voronoi.ridge_points
            assert [1, 2] in pix.voronoi.ridge_points or [2, 1] in pix.voronoi.ridge_points
            assert [3, 4] in pix.voronoi.ridge_points or [4, 3] in pix.voronoi.ridge_points
            assert [4, 5] in pix.voronoi.ridge_points or [5, 4] in pix.voronoi.ridge_points
            assert [6, 7] in pix.voronoi.ridge_points or [7, 6] in pix.voronoi.ridge_points
            assert [7, 8] in pix.voronoi.ridge_points or [8, 7] in pix.voronoi.ridge_points

            assert [0, 3] in pix.voronoi.ridge_points or [3, 0] in pix.voronoi.ridge_points
            assert [1, 4] in pix.voronoi.ridge_points or [4, 1] in pix.voronoi.ridge_points
            assert [4, 7] in pix.voronoi.ridge_points or [7, 4] in pix.voronoi.ridge_points
            assert [2, 5] in pix.voronoi.ridge_points or [5, 2] in pix.voronoi.ridge_points
            assert [5, 8] in pix.voronoi.ridge_points or [8, 5] in pix.voronoi.ridge_points
            assert [3, 6] in pix.voronoi.ridge_points or [6, 3] in pix.voronoi.ridge_points

    class TestNeighbors:
        def test__compare_to_pixelization_util(self):
            # 9 points in a square - makes a square (this is the example int he scipy documentaiton page)

            grid = np.array(
                [
                    [3.0, 0.0],
                    [2.0, 1.0],
                    [2.0, 2.0],
                    [8.0, 3.0],
                    [1.0, 3.0],
                    [1.0, 9.0],
                    [6.0, 31.0],
                    [0.0, 2.0],
                    [3.0, 5.0],
                ]
            )

            pix = aa.pix_grid.VoronoiGrid(grid_1d=grid)

            voronoi = scipy.spatial.Voronoi(
                np.asarray([grid[:, 1], grid[:, 0]]).T, qhull_options="Qbb Qc Qx Qm"
            )
            pixel_neighbors_util, pixel_neighbors_size_util = aa.util.pixelization.voronoi_neighbors_from_pixels_and_ridge_points(
                pixels=9, ridge_points=np.array(voronoi.ridge_points)
            )

            assert (pix.pixel_neighbors == pixel_neighbors_util).all()
            assert (pix.pixel_neighbors_size == pixel_neighbors_size_util).all()
