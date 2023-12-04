package top.atluofu.fsm;

import java.io.File;

/**
 * @ClassName: BatchDelFile
 * @description: 批量删除文件
 * @author: 有罗敷的马同学
 * @datetime: 2023Year-12Month-02Day-15:39
 * @Version: 1.0
 */
public class BatchDelFile {
    public static void main(String[] args) {
        String directoryPath = "D:\\迅雷云盘\\英语四级历年真题答案（含2023.6月最新真题）";
        String fileName = "福利! 19元255G手机流量卡免费领.docx";

        File directory = new File(directoryPath);
        deleteFiles(directory, fileName);
    }

    public static void deleteFiles(File directory, String fileName) {
        if (directory.isDirectory()) {
            File[] files = directory.listFiles();
            if (files != null) {
                for (File file : files) {
                    if (file.isDirectory()) {
                        deleteFiles(file, fileName); // 递归调用删除子目录下的文件
                    } else if (file.getName().equals(fileName)) {
                        file.delete(); // 删除指定文件
                        System.out.println("已删除文件: " + file.getAbsolutePath());
                    }
                }
            }
        }
    }
}
