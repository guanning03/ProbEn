python demo/FLIR/demo_FLIR_save_predictions.py \
--model_path trained_models/FLIR/models/FLIR_early_fusion.pth \
--rgb_path data/FLIR/RGB-test/ \
--thermal_path data/FLIR/IR-test/ \
--fusion_method early_fusion \
--outfolder predictions/FLIR/early_fusion/ 