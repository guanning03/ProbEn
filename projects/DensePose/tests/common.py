# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import os
import torch

from detectron1.config import get_cfg
from detectron1.engine import default_setup
from detectron1.modeling import build_model

from densepose import add_densepose_config

_BASE_CONFIG_DIR = "configs"
_QUICK_SCHEDULES_CONFIG_SUB_DIR = "quick_schedules"
_CONFIG_FILE_PREFIX = "densepose_"
_CONFIG_FILE_EXT = ".yaml"


def _get_base_config_dir():
    """
    Return the base directory for configurations
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", _BASE_CONFIG_DIR)


def _get_quick_schedules_config_dir():
    """
    Return the base directory for quick schedules configurations
    """
    return os.path.join(_get_base_config_dir(), _QUICK_SCHEDULES_CONFIG_SUB_DIR)


def _collect_config_files(config_dir):
    """
    Collect all configuration files (i.e. densepose_*.yaml) directly in the specified directory
    """
    start = _get_base_config_dir()
    results = []
    for entry in os.listdir(config_dir):
        _, ext = os.path.splitext(entry)
        if ext != _CONFIG_FILE_EXT:
            continue
        if not entry.startswith(_CONFIG_FILE_PREFIX):
            continue
        path = os.path.join(config_dir, entry)
        config_file = os.path.relpath(path, start)
        results.append(config_file)
    return results


def get_config_files():
    """
    Get all the configuration files (relative to the base configuration directory)
    """
    return _collect_config_files(_get_base_config_dir())


def get_quick_schedules_config_files():
    """
    Get all the quick schedules configuration files (relative to the base configuration directory)
    """
    return _collect_config_files(_get_quick_schedules_config_dir())


def _get_model_config(config_file):
    """
    Load and return the configuration from the specified file (relative to the base configuration
    directory)
    """
    cfg = get_cfg()
    add_densepose_config(cfg)
    path = os.path.join(_get_base_config_dir(), config_file)
    cfg.merge_from_file(path)
    if not torch.cuda.is_available():
        cfg.MODEL_DEVICE = "cpu"
    return cfg


def get_model(config_file):
    """
    Get the model from the specified file (relative to the base configuration directory)
    """
    cfg = _get_model_config(config_file)
    return build_model(cfg)


def setup(config_file):
    """
    Setup the configuration from the specified file (relative to the base configuration directory)
    """
    cfg = _get_model_config(config_file)
    cfg.freeze()
    default_setup(cfg, {})
