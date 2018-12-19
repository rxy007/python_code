# huffman code 

class Node(object):
    def __init__(self, weight, key=None):
        self.weight = weight
        self.key = key
        self.lnode = None
        self.rnode = None
        self.code = ['0'] # '0'表示左 '1'表示右

def build_huffman_tree(list_node):
    # 参数：node对象列表 按照权重逆序排序
    # 取权重最小的两个node 构建新的权重为两个权重之和
    if len(list_node) != 1:
        node_1 = list_node.pop()
        node_2 = list_node.pop()
        node_2.code = ['1']
        node_3 = Node(node_1.weight + node_2.weight)
        node_3.lnode = node_1
        node_3.rnode = node_2
        l = len(list_node)
        for i in range(l-1, -1, -1):
            if list_node[i].weight>= node_3.weight:
                list_node.insert(i+1, node_3)
                break
        if l == 0:
            list_node.insert(0, node_3)
        build_huffman_tree(list_node)
    return list_node[0]

def print_huffman_code(node):
    # 打印huffman 编码
    # 先将root节点的code插入到左子节点和右子节点
    if node:
        if node.rnode and node.lnode:
            for code in node.code:
                node.lnode.code.insert(-1, code)
                node.rnode.code.insert(-1, code)
        print_huffman_code(node.lnode)
        if node.key:
            node.code.pop(0)
            print(node.weight, node.key, ''.join(node.code))
        print_huffman_code(node.rnode)

if __name__ == "__main__":
    import collections
    s = '0000000000000000000000000000000000000000000000000000000300000000020168000000008060000000002038000000000815600000000306fc00000000e03f800000007c0fe00000003f03f80000000d40fe00000003603b80000000f80fa00000003e1a700000000f85fe00000003c1ff80000001e03fe0000000700ff80000001c038400000007006080000003c01ac0000000f006f00000003801fc0000000e006f000000078031c0000001e00c200000007803000000001e01e20000000f81f980000003e3fe60000000f1ff700000003cfeea0000000ffffec0000007f7fff8000001fefff70000007fdfffe000001fe7fff8000007fcffff000001ff3fffc000007f87fff000001fe1fffc000007f83fff0000007c07ffc000000401fff0000000003ffc0000000007ff0000000001ffe0000'
    frequency = collections.Counter(s)
    list_node = []
    for k, v in frequency.items():
        list_node.append(Node(v, k))
    list_node = sorted(list_node, key=lambda node: node.weight, reverse=True)
    huffman_tree = build_huffman_tree(list_node)
    print(huffman_tree.weight)
    print_huffman_code(huffman_tree)
