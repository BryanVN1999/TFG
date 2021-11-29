package com.example.heartapp;

import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.google.android.material.snackbar.Snackbar;

public class UserActivity extends AppCompatActivity {
    EditText name, surname;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user);
        Button continueButton = findViewById(R.id.saveButton);
        name = findViewById(R.id.name);
        surname = findViewById(R.id.surname);
        continueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!isBlankString(name.getText().toString()) && !isBlankString(surname.getText().toString()))
                {
                    GraphsActivity.NameUser = name.getText().toString();
                    GraphsActivity.SurnameUser = surname.getText().toString();
                    Intent toGraphs = new Intent(v.getContext(), GraphsActivity.class);
                    startActivity(toGraphs);
                } else {
                    Snackbar mySnackbar = Snackbar.make(v, "Inserte su nombre y apellidos", Snackbar.LENGTH_SHORT);
                    mySnackbar.show();
                }
            }
        });
    }
    private boolean isBlankString(String string)
    {
        return string == null || string.isEmpty() || string.trim().isEmpty();
    }
}