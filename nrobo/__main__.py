"""
Entry point for nrobo framework
"""

import sys

if __name__ == '__main__':
    # Trigger point for nrobo command line utility
    from nrobo.cli import main

    sys.exit(main())