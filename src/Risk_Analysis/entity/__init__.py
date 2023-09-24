from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_dir : Path
    train_dir : Path
    test_dir :Path


@dataclass(frozen=True)
class DataTransformationConfig:
    transformation_dir:Path
    preprocessor_dir :Path