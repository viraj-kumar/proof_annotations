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
var_1 = Variant()  # Create a default Variant (minimum value: 0)

i = 1
while i <= 10:
    var_1(10 - i)  # This expression strictly decreases in each
                   # iteration, starting from some initial value
    i += 1


# Example 2: Observe the values of the Variant as the loop iterates.
var_2 = Variant('var_2', lower_bound=1, debug=True)  # Variant 'var_2' (minimum value: 1)

i = 1
while i <= 10:
    var_2(10 - i)  # This expression is eventually less than the
                   # minimum value, leading to an error.
    i += 1
```

Adjust the API call to match the utility methods exposed by your package.

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