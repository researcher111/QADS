__author__ = 'Daniel'

import QuerySignatures
import Engine
import ResultParser


def main():

    print ResultParser.Parser.parse(Engine.QueryExecuter.excuteQuery(QuerySignatures.Signatures.hosts()))

if __name__ == "__main__":
    main()


