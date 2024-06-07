python demo/FLIR/demo_FLIR_save_predictions.py \
--model_path trained_models/FLIR/models/FLIR_thermal_only.pth \
--rgb_path data/one/rgb \
--thermal_path data/one/thermal \
--fusion_method thermal_only \
--outfolder predictions/one/thermal_only/ 