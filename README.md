# Turkana Drought Monitoring

A Python and Google Earth Engine workshop for reviewing drought-index rasters and calculating monthly drought indicators for Turkana County, Kenya. The main notebook is [`drought_monitoring.ipynb`](drought_monitoring.ipynb); [`droughtMonitoring.ipynb`](droughtMonitoring.ipynb) is also included in the repository.

## What it does

- Reviews multiband annual PDI, TDI, VDI, and CDI GeoTIFFs.
- Summarizes annual spatial means and maps annual CDI values.
- Optionally retrieves monthly climate and vegetation data from Earth Engine.
- Calculates a three-month seasonal-ratio CDI, plots time-series and seasonal summaries, and produces an exploratory six-month forecast.
- Saves figures and tables under `Outputs/` without overwriting source rasters.

The composite index uses the reference weights:

```text
CDI = 0.50 * PDI + 0.25 * TDI + 0.25 * VDI
```

The supplied severity guide classifies CDI below 0.50 as extreme drought, 0.50-0.65 severe, 0.65-0.80 moderate, 0.80-0.90 mild, 0.90-1.10 near normal, 1.10-1.20 mild wet, 1.20-1.30 moderately wet, and above 1.30 very wet.

## Setup

Use Python 3.10 or newer and Jupyter support in VS Code or JupyterLab. From the project directory, install the notebook dependencies:

```powershell
python -m pip install earthengine-api geemap rasterio numpy pandas matplotlib statsmodels
python -m pip install "drought-monitoring[all]"
```

Open `drought_monitoring.ipynb` and run its package-install cells if you prefer to install from inside the notebook. Set the Earth Engine project in the authentication cell to a Google Cloud project registered for Earth Engine, then complete the browser sign-in when prompted. The cached-raster review does not require Earth Engine authentication; the live data section does.

## Outputs

The notebook writes these requested figures to `Outputs/`:

- `CDI_annual_maps.png` - annual CDI map panels for 2000-2025.
- `CDI_annual_Turkana.png` - annual area-weighted Turkana CDI.
- `CDI_seasonal_Turkana.png` - DJF, MAM, JJA, and SON CDI summaries across complete seasons.
- `CDI_timeseries_Turkana.png` - monthly CDI with a 12-month mean.

Additional notebook figures and CSV tables are also saved to the same folder.

## Data and interpretation notes

The live workflow uses the GAUL 2025 level-1 Turkana boundary, ERA5-Land monthly precipitation and 2 m temperature, and MODIS/061/MOD13A3 monthly NDVI. Precipitation is converted from metres to millimetres, temperature from kelvin to Celsius, and MODIS NDVI uses its 0.0001 scale factor.

For the live CDI, the temperature ratio is inverted so that unusually warm conditions lower the score, aligning heat stress with rainfall and vegetation deficits. The notebook uses a three-month seasonal ratio and does not include the run-length multiplier shown in the reference formula. Saved GeoTIFFs are interpreted as supplied and are not recalculated by the live workflow, so their CDI values may differ.

The six-month Holt-Winters projection is exploratory, has no prediction interval, and is not an operational drought warning. County-wide averages and the supplied coarse raster grid can hide local drought conditions. Validate the method and thresholds against local observations before using them for decisions.

## Current raster availability

The cached-raster section expects these four files in `Outputs/`:

```text
Turkana_2000_2025_CDI.tif
Turkana_2000_2025_PDI.tif
Turkana_2000_2025_TDI.tif
Turkana_2000_2025_VDI.tif
```

At the time this README was added, the repository contains the Turkana TDI and VDI rasters, but the CDI and PDI GeoTIFFs are absent. Restore those two source rasters to run the cached-raster section from a fresh clone. The live Earth Engine workflow can fetch data independently, subject to Earth Engine access.
