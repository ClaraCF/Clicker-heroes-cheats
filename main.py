import argparse
import base64
import zlib


def insert(string: str, source: str, pos: int):
    return source[:pos] + string + source[pos:]


def remove(source: str, start: int, end: int):
    return source[:start] + source[end:]


parser = argparse.ArgumentParser()

# help menu
gold_help = "specifies a new amount of gold"
rubies_help = "specifies a new amount of rubies"
hero_help = "specifies a new amount of hero souls"
output_help = "Output result to a file instead of the screen"

parser.add_argument("-g", dest="gold", type=float, help=gold_help, default=None, metavar="gold amount")
parser.add_argument("-r", dest="rubies", type=float, help=rubies_help, default=None, metavar="rubies amount")
parser.add_argument("-s", dest="souls", type=float, help=hero_help, default=None, metavar="souls amount")
parser.add_argument("-o", dest="output", type=str, help=output_help, default=None, metavar="filename")
parser.add_argument("--stdin", action="store_true", help="Takes base64 input from stdin instead of a file")
parser.add_argument("save", type=str, help="The path to your exported Base64 game save file")

argv = parser.parse_args()

if argv.gold is None and argv.rubies is None and argv.souls is None:
    print("[-] Nothing to do. Exiting...")
    exit(0)

save: bytes = b''

if argv.stdin:
    save = argv.save.encode('utf-8')

else:
    with open(argv.save, "rb") as file:
        save = file.read()

decoded_binary = base64.b64decode(save)
header = decoded_binary[:24]
decoded_binary = decoded_binary[24:]

code = zlib.decompress(decoded_binary).decode('utf-8')

if argv.gold is not None:
    gold_start_index = code.find("gold\"") + 7
    gold_end_index = 0
    i = gold_start_index

    for char in code[gold_start_index:code.__len__()]:
        i += 1
        if char == '"':
            gold_end_index = i - 1
            break

    code = remove(code, gold_start_index, gold_end_index)
    code = insert(str(argv.gold), code, gold_start_index)

if argv.rubies is not None:
    rubies_start_index = code.find("rubies\"") + 8
    rubies_end_index = 0

    i = rubies_start_index
    for char in code[rubies_start_index:code.__len__()]:
        i += 1
        if char == ',':
            rubies_end_index = i - 1
            break

    code = remove(code, rubies_start_index, rubies_end_index)
    code = insert(str(argv.rubies), code, rubies_start_index)

if argv.souls is not None:
    souls_start_index = code.find("heroSouls\"") + 12
    souls_end_index = 0

    i = souls_start_index
    for char in code[souls_start_index:code.__len__()]:
        i += 1
        if char == '"':
            souls_end_index = i - 1
            break

    code = remove(code, souls_start_index, souls_end_index)
    code = insert(str(argv.souls), code, souls_start_index)

compressed_code = zlib.compress(code.encode('utf-8'), 9)
final = header + compressed_code

if argv.output is not None:
    with open(argv.output, "w") as file:
        file.write(base64.b64encode(final).decode('utf-8') + '\n')
        file.close()
    exit(0)

print(base64.b64encode(final).decode('utf-8'))
