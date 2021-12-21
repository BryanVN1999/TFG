package com.example.heartapp;

import android.content.Intent;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class GraphsActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_graphs);
        Button ecg, spo2;
        ecg = findViewById(R.id.ecg);
        spo2 = findViewById(R.id.spo2);

        ecg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent toEcg = new Intent(v.getContext(), EcgActivity.class);
                startActivity(toEcg);
            }
        });

        spo2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent toSpo2 = new Intent(v.getContext(), Spo2Activity.class);
                startActivity(toSpo2);
            }
        });
    }
}