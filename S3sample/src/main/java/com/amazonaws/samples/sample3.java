package com.amazonaws.samples;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AmazonS3Exception;
import com.amazonaws.services.s3.model.Bucket;

public class sample3 {
    public static Bucket getBucket(String bucket_name) {
        final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.DEFAULT_REGION).build();
        Bucket named_bucket = null;
        List<Bucket> buckets = s3.listBuckets();
        for (Bucket b : buckets) {
            if (b.getName().equals(bucket_name)) {
                named_bucket = b;
            }
        }
        return named_bucket;
    }

    public static Bucket createBucket(String bucket_name) {
        final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.DEFAULT_REGION).build();
        Bucket b = null;
        if (s3.doesBucketExistV2(bucket_name)) {
            System.out.format("Bucket %s already exists.\n", bucket_name);
            b = getBucket(bucket_name);
        } else {
            try {
                b = s3.createBucket(bucket_name);
            } catch (AmazonS3Exception e) {
                System.err.println(e.getErrorMessage());
            }
        }
        return b;
    }

    public static void main(String[] args) {
        final String USAGE = "\n" +
                "CreateBucket - create an S3 bucket\n\n" +
                "Usage: CreateBucket <bucketname>\n\n" +
                "Where:\n" +
                "  bucketname - the name of the bucket to create.\n\n" +
                "The bucket name must be unique, or an error will result.\n";

        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
 
        System.out.println("バケットの名前をキーボードから入力してください");
 
        String str = null;
        try {
            str = br.readLine();
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
 
        System.out.println("入力された文字は「" + str + "」です");
        
        String name[];
        name = new String[1];
        
        name[0] = str ;    
        
        if (name.length < 1) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String bucket_name = name[0];

        System.out.format("\nCreating S3 bucket: %s\n", bucket_name);
        Bucket b = createBucket(bucket_name);
        if (b == null) {
            System.out.println("Error creating bucket!\n");
        } else {
            System.out.println("Done!\n");
        }
    }
}