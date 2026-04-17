# proof_annotations

`proof_annotations` is a lightweight Python package that provides annotation for:
- Proving termination (using `Variant`)
- Proving correctness (using `Invariant`)

## Installation

Install directly from GitHub using `pip`:

```bash
pip install git+https://github.com/viraj-kumar/proof_annotations.git
```

## Usage

```python
from proof_annotations import Variant

# Example 1: Use a Variant to prove that this while-loop terminates.
var_1 = Variant()  # A default Variant (minimum value: 0)

i = 1
while i <= 10:
    var_1(10 - i)  # The expression (10 - i) strictly decreases (from
                   # some initial value) in each iteration
    i += 1


# Example 2: Observe the values of the Variant as the loop iterates.
var_2 = Variant('var_2', lower_bound=1, debug=True)  # Variant 'var_2' with
                                                     # debug information and
                                                     # minimum value: 1

i = 1
while i <= 10:
    var_2(10 - i)  # The expression (10 - i) is eventually less than the
                   # minimum value (1), leading to an error
    i += 1
```

## Project Structure

```text
proof_annotations/
├── proof_annotations.py   # Annotation utility classes
├── __init__.py            # Public API exports
└── README.md
```

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.