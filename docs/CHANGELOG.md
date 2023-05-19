# Changelog
All notable changes to this project will be documented in this file.

## [0.3.4] - 2023-05-19
### Added
- System utilities (debug):
  - `output ( )`

### Changed
- Custom utilities (validation): refactored & optimized
  - `is_cached_file_old ( )`

- System utilities (time):
  - `get_current_timestamp ( )` >> changed to >> `get_enumerated_timestamp ( )`

## [0.3.3] - 2023-05-18
### Added
- Custom utilities (prompt):
  - `get_completion ( )`
  - `query_completion ( )`

- System utilities (time):
  - `get_current_timestamp ( )`

### Changed
- Migrated the following functions to `utilities/custom/model`
  - `fetch_models ( )`
  - `get_models ( )`
  - `parse_model ( )`
  - `parse_models ( )`

### Removed
- System utilities (validation)
  - `is_flag ( )`

- System utilities (general)
  - `get_command_type ( )`

## [0.2.2] - 2023-05-15
### Added
- Implemented AI model selection via command line and from `config.txt`

- Custom utilities (general)
  - `fetch_models ( )`

- Custom utilities (file):
  - `read_from_cache ( )`
  - `write_to_cache ( )`

- Custom utilities (validation):
  - `is_cached_file ( )`

### Changed
- Custom utilities (connect):
  - `openai_connect ( )` >> changed to >> `openai_certify ( )`

- Custom utilities (general):
  - `parse_list_models ( )` >> changed to >> `parse_models ( )` & `parse_model ( )`
  - `get_list_models ( )`   >> changed to >> `get_models ( )`

### Removed
- Custom utilities (file)
  - `write_file ( )`

## [0.2.1] - 2023-05-10
### Added
- Custom utilities (file):
  - `write_file ( )`

- Custom utilities (general):
  - `get_list_models ( )`

- Folders
  - `cache` directory data assets

### Changed
- Custom utilities (general):
  - `get_list_models ( )` >> changed to >> `parse_list_models ( )`

## [0.2.0] - 2023-05-09
### Added
- Custom utilities (connect):
  - `openai_connect ( )`

### Changed
- Refactored & refined:
  - `get_command_type ( )`
  - `parse_commands ( )`
  - `util.py`
  - `test-utilities.py`
  - `main.py`

## [0.1.0] - 2023-05-08
### Added
- System utilities (general):
  - `get_command_type ( )`
  - `get_commands ( )`
  - `parse_commands ( )`

- System utilities (validation):
  - `is_directory ( )`
  - `is_file ( )`
  - `is_flag ( )`

- Files:
  - `util.py`
  - `test-utilities.py`

- Folders
  - `images` directory with two byrne-systems image assets

## [0.0.0] - 2023-05-08
### Added
- Directory structure
- main.py
- License
- `README.md`

---

| Version | Date       | Commit                                                            | Comments 														                             |
| :-----: | :--------: | :---------------------------------------------------------------: | :---------------------------------------------------------------- |
| 0.3.4   | 2023-05-19 | Current                                                           | General refactoring; implemented output debugging module
| 0.3.3   | 2023-05-18 | [ffd1084](https://github.com/Justin-Byrne/ChatGpt/commit/ffd1084) | Completion query implementation, with minor refactoring
| 0.2.2   | 2023-05-15 | [1b056fd](https://github.com/Justin-Byrne/ChatGpt/commit/1b056fd) | Implemented AI model selection via command line and from `config.txt`
| 0.2.1   | 2023-05-10 | [cc77804](https://github.com/Justin-Byrne/ChatGpt/commit/cc77804) | Implemented basic cache system, and general refactoring
| 0.2.0   | 2023-05-09 | [0bb4157](https://github.com/Justin-Byrne/ChatGpt/commit/0bb4157) | Implemented OpenAI connection & authentication
| 0.1.0   | 2023-05-08 | [bf8ffc6](https://github.com/Justin-Byrne/ChatGpt/commit/bf8ffc6) | Implemented system utilities & validation methods
| 0.0.0   | 2023-05-08 | [447d129](https://github.com/Justin-Byrne/ChatGpt/commit/447d129) | initial upload

---

## Types of changes
- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ChatGpt/blob/main/images/byrne-systems.logo.png)

==Byrne-Systems © 2023 - All rights reserved.==
