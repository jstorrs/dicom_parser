"""
Definition of the :attr:`SEQUENCE_TO_BIDS` dictionary.
"""
from dicom_parser.utils.bids.header_queries import (
    find_irepi_acq,
    find_mprage_acq,
    find_phase_encoding,
    find_task_name,
)

# Dictionaries (`Dict[str, Union[str, Callable]]``) associating MR sequences
# with BIDS key/value pairs.
BOLD = {
    "data_type": "func",
    "task": find_task_name,
    "dir": find_phase_encoding,
    "suffix": "bold",
}
DWI = {
    "data_type": "dwi",
    "dir": find_phase_encoding,
    "suffix": "dwi",
}
DWI_SBREF = {
    "data_type": "dwi",
    "acq": "dwi",
    "dir": find_phase_encoding,
    "suffix": "sbref",
}
FLAIR = {"data_type": "anat", "suffix": "FLAIR"}
FUNCTIONAL_FIELDMAP = {
    "data_type": "fmap",
    "acq": "func",
    "dir": find_phase_encoding,
    "suffix": "epi",
}
FUNCTIONAL_SBREF = {
    "data_type": "func",
    "task": find_task_name,
    "dir": find_phase_encoding,
    "suffix": "sbref",
}
IREPI = {"data_type": "anat", "inv": find_irepi_acq, "suffix": "IRT1"}
MPRAGE = {"data_type": "anat", "ce": find_mprage_acq, "suffix": "T1w"}
SPGR = {"data_type": "anat", "acq": "spgr", "suffix": "T1w"}
FSPGR = {"data_type": "anat", "acq": "fspgr", "suffix": "T1w"}
T2W = {"data_type": "anat", "ce": find_mprage_acq, "suffix": "T2w"}

#: BIDS fields used in Magnetic Resonance (MR) imaging and their associated
#: definitions.
MR_SEQUENCE_TO_BIDS = {
    "mprage": MPRAGE,
    "spgr": SPGR,
    "fspgr": FSPGR,
    "ir_epi": IREPI,
    "t2w": T2W,
    "flair": FLAIR,
    "bold": BOLD,
    "func_sbref": FUNCTIONAL_SBREF,
    "func_fieldmap": FUNCTIONAL_FIELDMAP,
    "dwi": DWI,
    "dwi_sbref": DWI_SBREF,
}
#: Known BIDS field values by modality.
SEQUENCE_TO_BIDS = {"Magnetic Resonance": MR_SEQUENCE_TO_BIDS}
