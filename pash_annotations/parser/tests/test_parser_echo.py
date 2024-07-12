from pash_annotations.datatypes.CommandInvocationInitial import CommandInvocationInitial
from pash_annotations.parser.parser import parse

# This is solely to test whether commands with the empty string as an operand
# such as echo "" function properly
def test_echo_1():
    parser_result = parse('echo ""')

    args = []
    operands = []
    expected_result = CommandInvocationInitial("echo", args, operands)

    assert expected_result == parser_result
