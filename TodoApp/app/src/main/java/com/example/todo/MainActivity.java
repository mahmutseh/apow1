package com.example.todo;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.EditText;
import android.widget.Button;
import android.view.View;
import java.util.ArrayList;

public class MainActivity extends Activity {
    private ArrayList<String> items;
    private ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        items = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, items);
        ListView listView = findViewById(R.id.listView);
        listView.setAdapter(adapter);

        EditText input = findViewById(R.id.input);
        Button addButton = findViewById(R.id.addButton);
        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = input.getText().toString();
                if (!text.isEmpty()) {
                    items.add(text);
                    adapter.notifyDataSetChanged();
                    input.setText("");
                }
            }
        });
    }
}
