package test;

public class LinkedListSort {

    private ListNode findHalf(ListNode head) {
        ListNode slow,fast;
        slow = fast = head;
        while (fast!=null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
    
    private ListNode merge(ListNode first, ListNode second) {
        ListNode ret,pre,tmp;
        if (first == null || second == null) {
            return (first == null)?second:first;
        }
        ret = (first.val>second.val)?second:first;
        // to avoid compiler's warning, add "tmp =".
        tmp = (first.val>second.val)?(second=second.next):(first=first.next);
        pre = ret;
        while (first == null || second == null) {
            if (first.val < second.val) {
                pre.next = first;
                first = first.next;
            }else {
                pre.next = second;
                second = second.next;
            }
        }
        pre.next = (first == null)?second:first;
        return ret;
        
    }
    
    public ListNode sortMerge(ListNode head) {
        ListNode first,second,ret;
        first = head;
        if (head == null || head.next == null) {
            return head;
        }
        
        second = findHalf(head);
        if (first != null) {
            first = sortMerge(first);
        }
        if (second != null) {
            second = sortMerge(second);
        }
        ret = merge(first,second);
        return ret;
        
    }
    
    public ListNode sortInsert(ListNode head) {

        ListNode pre,cur,next;
        if (head == null || head.next == null) {
            return head;
        }
        if (head.val < head.next.val) {
            return head;
        }
        pre = head;
        cur = pre.next;
        next = cur.next;
        
        //insert sort to be finished.
        return null;
        
    }
    public static void main(String[] args) {
        
        ListNode l1 = new ListNode(3);
        ListNode l2 = new ListNode(27);
        ListNode l3 = new ListNode(16);
        ListNode l4 = new ListNode(53);
        ListNode l5 = new ListNode(9);
        ListNode l6 = new ListNode(81);
        
        l1.next = l2;
        l2.next = l3;
        l3.next = l4;
        l4.next = l5;
        l5.next = l6;
        l6.next = null;
        
        ListNode ret;
        LinkedListSort lls = new LinkedListSort();
        ret = lls.sortMerge(l1);
        ListNode tmp;
        tmp = ret;
        while (tmp != null) {
            System.out.println(tmp.val);
            tmp = tmp.next;
        }
    }
}

class ListNode {
    
    public int val;
    public ListNode  next;
    
    
    public ListNode(int value) {
        val = value;
    }
    
}
