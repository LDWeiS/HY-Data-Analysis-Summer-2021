#!/usr/bin/env python3

from os import linesep


def file_extensions(filename):
    files = []
    extDict = {}

    with open(filename, "r") as f:
        for line in f:
            lineStrip = line.rstrip()
            lineSplit = lineStrip.split(".")

            if len(lineSplit) == 1:
                files.append(lineStrip)
                break

            if lineSplit[-1] not in extDict:
                extDict[lineSplit[-1]] = [lineStrip]
            else:
                extDict[lineSplit[-1]].append(lineStrip)

    return (files, extDict)

def main():
    noExt, extDict = file_extensions("src/filenames.txt")
    print(f"{len(noExt)} files with no extension")
    for k, v in extDict.items():
        print(f"{k} {len(v)}")

if __name__ == "__main__":
    main()
