public class LowestCommonAncester {

    public TreeNode lowestCommonAncester(TreeNode node1, TreeNode node2) {
        // find root and count length of path
        int path_length1 = 0;
        int path_length2 = 0;
        TreeNode tmp1;
        TreeNode tmp2;
        if (node1 == node2) {
            return node1;
        }
        
        tmp1 = node1;
        while (tmp1.parent != null) {
            tmp1 = tmp1.parent;
            path_length1 += 1;
        }
        tmp2 = node2;
        while (tmp2.parent!=null) {
            tmp2 = tmp2.parent;
            path_length2 += 1;
        }
        //TreeNode tmp;
        if (path_length1==path_length2){
            tmp1 = node1;
            tmp2 = node2;
            while (tmp1 != tmp2) {
                tmp1 = tmp1.parent;
                tmp2 = tmp2.parent;
            }
            return tmp1;
        } else {
            if (path_length1>path_length2) {
                int distance = path_length1-path_length2;
                tmp1 = node1;
                while (distance > 0) {
                    tmp1 = tmp1.parent;
                    distance -= 1;
                }
                tmp2 = node2;
                while (tmp1!=tmp2) {
                    tmp1 = tmp1.parent;
                    tmp2 = tmp2.parent;
                }
            } else {
                int distance = path_length2 - path_length1;
                tmp2 = node2;
                while(distance > 0) {
                    tmp2 = tmp2.parent;
                }
                tmp1 = node1;
                while (tmp1!= tmp2) {
                    tmp1 = tmp1.parent;
                    tmp2 = tmp2.parent;
                }
            }
            return tmp1;
        }
        
    }
    
}