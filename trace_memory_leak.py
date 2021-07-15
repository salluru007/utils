import tracemalloc

tracemalloc.start(2)
start = tracemalloc.take_snapshot()
prev = start

def trace_leak(self, start, prev, top=20):
        current = tracemalloc.take_snapshot()
        stats = current.compare_to(start, 'filename')
        prev_stats = current.compare_to(prev, 'lineno')

        for i, stat in enumerate(stats[:top], 1):
            print(f"top diffs i={i}, stat={stat}")

        for i, stat in enumerate(prev_stats[:top], 1):
            print(f"top incremental i={i}, stat={stat}")

        for i, stat in enumerate(current.statistics('filename')[:top], 1):
            print(f"top current i={i}, stat={stat}")

        traces = current.statistics('traceback')
        for stat in traces[:2]:
            print(f"traceback memory_blocks={stat.count}, size_kB={stat.size/1024}")
            for line in stat.traceback.format():
                print(line)
        return prev
