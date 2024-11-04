import netCDF4 as nc
from netCDF4 import num2date
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np


class EDDY:
    def __init__(self, filename):
        self.df = nc.Dataset(filename)
        breakpoint()


    def subset_velocity(self):
        1+1;


    def subset_META(self):

        indx = int(2.18e06)

        area = [-50, -42, -58, -30]
        lon = self.df['longitude'][indx::] - 180
        id_lon = (lon < -30) & (lon > -42)

        lat = self.df['latitude'][indx::]
        id_lat = (lat< -50) & (lat > -58)

        id_geo = id_lat & id_lon
        t_units = self.df['time'].units

        t_frame = self.df['time'][indx::]
        amplitude = self.df['amplitude'][indx::]

        e_radius = self.df['effective_radius'][indx::]


        lon2 = lon[id_geo]
        lat2 = lat[id_geo]
        amp2 = amplitude[id_geo]

        lat_bin_vals = np.linspace(-58, -50, 50)
        lon_bin_vals = np.linspace(-42, -30, 50)
        bin_lat = np.digitize(lat2, lat_bin_vals)
        bin_lon = np.digitize(lon2, lon_bin_vals)
        amp_mat = np.zeros([lon_bin_vals.shape[0], lat_bin_vals.shape[0]])
        for i in range(0, lon2.shape[0]):
            amp_mat[bin_lon[i], bin_lat[i]] = amp2[i]


        #breakpoint()

        #breakpoint()

        fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
        fig1 = axs.pcolormesh(lon_bin_vals, lat_bin_vals, amp_mat.T, cmap=plt.get_cmap('Reds'), transform=ccrs.PlateCarree())
        axs.coastlines()
        fig.colorbar(fig1, label='amplitude' + ' units =' + 'm')
        # axs.set_title('long_name = ' + var.long_name)
        axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
        # axs.set_extent([0, 100, 0, 100])
        plt.show()
        breakpoint()

        time = num2date(t_frame, t_units)


