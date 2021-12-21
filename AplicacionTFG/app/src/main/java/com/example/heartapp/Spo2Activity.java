package com.example.heartapp;

import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class Spo2Activity extends AppCompatActivity {
    public static String NameUser, SurnameUser;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spo2);
        TextView user = findViewById(R.id.user);
        user.setText(NameUser + " " + SurnameUser);
    }
}